def copy_file(command: str) -> None:
    words = command.split()
    first_file, second_file = words[1], words[2]

    if first_file == second_file:
        return

    with open(first_file, "r") as file_in, open(second_file, "w") as file_out:
        file_out.write(file_in.read())
