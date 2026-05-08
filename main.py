import student
import utils

def main():
    while True:
        utils.display_menu()
        choice = input("Chon chuc nang (1-5): ")

        if choice == '1':
            s_id = input("Nhap ID sinh vien: ")
            s_name = input("Nhap ten sinh vien: ")
            s_major = input("Nhap chuyen nganh: ")
            success = student.add_student(s_id, s_name, s_major)
            if success:
                print("Them thanh cong!")
            else:
                print("ID da ton tai, them that bai.")
        elif choice == '2':
            all_s = student.get_all_students()
            if not all_s:
                print("Danh sach trong.")
            else:
                print("Danh sach sinh vien:")
                for s in all_s:
                    utils.print_student(s)
        elif choice == '3':
            s_id = input("Nhap ID can tim: ")
            found = student.search_student_by_id(s_id)
            if found:
                print("Da tim thay:")
                utils.print_student(found)
            else:
                print("Khong tim thay sinh vien.")
        elif choice == '4':
            s_id = input("Nhap ID can xoa: ")
            success = student.delete_student(s_id)
            if success:
                print("Xoa thanh cong!")
            else:
                print("Khong tim thay sinh vien de xoa.")
        elif choice == '5':
            print("Ket thuc chuong trinh.")
            break
        else:
            print("Lua chon khong hop le, vui long thu lai.")

if __name__ == "_main_":
    main()