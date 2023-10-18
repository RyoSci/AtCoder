import subprocess
import os

os.makedirs("./out", exist_ok=True)

for i in range(1):
    a = subprocess.run(
        f"cargo run --release --bin tester ../Rust_code/a.out < in/{str(i).zfill(4)}.txt > out/out{str(i).zfill(i)}.txt".split())
