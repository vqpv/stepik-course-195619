def get_extensions(file_list):
    def _get_extension(file):
        if "." in file:
            ext = file.split(".")[-1]
        else:
            ext = ""
        return ext
    return [_get_extension(i) for i in file_list]
