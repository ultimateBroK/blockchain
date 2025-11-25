import sys
import hashlib

def compute_sha256(filename):
    sha256_hash = hashlib.sha256()

    try:        
        with open(filename, "rb") as f:
            while True:
                chunk = f.read(4096)
                if not chunk:
                    break
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return "Không tìm thấy file"
    except PermissionError:
        return "Quyền truy cập bị từ chối"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Cách dùng: python sha_256.py <input_file>")
        sys.exit(1)
        
    filename = sys.argv[1]
    
    print(compute_sha256(filename))