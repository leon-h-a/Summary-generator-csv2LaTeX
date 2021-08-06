def add_bash_alias(bash_aliases_path, alias_name, tex_file_path, filename):
    text = str((tex_file_path / filename).as_posix()).replace(" ", "\\ ")

    with open(bash_aliases_path, 'a') as aliases_file:
        aliases_file.write(
            "alias {}={}.tex".format(alias_name, text)
        )
