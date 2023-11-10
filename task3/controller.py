import os
import signal
import subprocess
import select

produced = 0

def signal_handler(signum, frame):
    global produced
    if signum == signal.SIGUSR1:
        print(f"Produced: {produced}")

def run_producer(pipe):
    os.dup2(pipe, 1)
    subprocess.run(["python3", "producer.py"])
    exit(0)

def run_calculator(pipe_in, pipe_out):
    os.dup2(pipe_in, 0)
    os.dup2(pipe_out, 1)
    os.execl("/usr/bin/bc", "bc")
    exit(0)

def main():
    pid = os.getpid()
    print(f"Started controller with PID: {pid}", flush=True)
    
    global produced
    produced = 0
    signal.signal(signal.SIGUSR1, signal_handler)

    pipe1, pipe0, pipe2 = os.pipe(), os.pipe(), os.pipe()

    p1 = os.fork()

    if p1 == 0:  # Child process P1
        os.close(pipe1[0])
        run_producer(pipe1[1])

    else:  # Parent process P0
        os.close(pipe1[1])
        p2 = os.fork()

        if p2 == 0:  # Child process P2
            os.close(pipe0[1])
            os.close(pipe2[0])
            run_calculator(pipe0[0], pipe2[1])

        else:  # Parent process P0
            os.close(pipe0[0])
            os.close(pipe2[1])

            results = []
            while True:
                rlist, _, _ = select.select([pipe1[0]], [], [], 1)
                if rlist:
                    expression = os.read(pipe1[0], 100).decode("utf-8").strip()
                    if not expression:
                        break

                    os.write(pipe0[1], expression.encode("utf-8") + b"\n")
                    produced += 1
                    result = os.read(pipe2[0], 100).decode("utf-8").strip()
                    results.append((expression, result))

                for expression, result in results:
                    print(f"{expression} = {result}")
                results = []

if __name__ == "__main__":
    main()
