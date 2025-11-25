# Viết chương trình nhận vào tên file, sau đó đọc và tính SHA-256 của nội dung file. 
# Chương trình nên viết ở dạng command line, tham số đầu vào là tên file. 
# Chương trình chỉ in ra một dòng duy nhất là Hash SHA-256 ở dạng hex. 
# Lưu ý: có thể sử dụng thư viện, không cần tự viết hàm tính SHA-256. 
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
        print("Cách dùng: python b2_sha_256.py <input_file>")
        sys.exit(1)
        
    filename = sys.argv[1]
    
    print(compute_sha256(filename))