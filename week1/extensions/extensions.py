def main():

    user_input = input("File name: ").strip().lower()
    split = user_input.split('.')
    filetype = split[-1]

    match filetype:
        case "jpg":
            print("image/jpeg")
        case "pdf":
            print("application/pdf")
        case "jpeg":
            print("image/jpeg")
        case "gif":
            print("image/gif")
        case "png":
            print("image/png")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")



if __name__ == "__main__":
    main()