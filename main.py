import student
import utils
import storage

def main():
    loaded = storage.load_data()
    student.set_students(loaded)
    print("Da tai du lieu thanh cong tu data.json.")

    while True:
        utils.display_menu()
        choice = input("Chon chuc nang (1-6): ")

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
            storage.save_data(student.get_all_students())
            print("Luu du lieu thanh cong vao file data.json.")
        elif choice == '6':
            storage.save_data(student.get_all_students())
            print("Da luu du lieu truoc khi thoat.")
            print("Ket thuc chuong trinh.")
            break
        else:
            print("Lua chon khong hop le, vui long thu lai.")

if __name__ == "__main__":
    main()