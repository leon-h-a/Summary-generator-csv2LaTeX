def add_bash_alias(bash_aliases_path, alias_name, tex_file_path, filename):
    alias_path = str((tex_file_path / filename / filename))

    with open(bash_aliases_path, 'a') as aliases_file:
        aliases_file.write(
            'alias {}="vim {}.tex"'.format(alias_name, alias_path
                                           ))
