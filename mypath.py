class Path(object):
    @staticmethod
    def db_root_dir(database):
        if database == 'pascal':
            return '/mnt/hdd/VOCdevkit/VOC2012/'  # folder that contains VOCdevkit/.
        elif database == 'sbd':
            return '/mnt/hdd/benchmark_RELEASE/' # folder that contains dataset/.
        elif database == 'lapvideos':
            return '/mnt/mlnasrw/Data/LapBypass/Sanjay/'  # folder that contains dataset/.
        else:
            print('Database {} not available.'.format(database))
            raise NotImplementedError

    @staticmethod
    def models_dir():
        return './models/'

