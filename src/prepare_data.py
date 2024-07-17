from src import utils


class PrepareData:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def rewrite_list(self):
        """
        Re-write the .json file contains phone prefix list to become a dict contains dial_code and its price.
        Example: {"93": 0.36}
        """
        data = utils.read_file(self.file_name)
        new_data = dict()

        for d in data:
            new_data[d["dial_code"]] = utils.random_float(2)

        utils.write_to_file(new_data, self.file_name)
