__author__ = 'vpyvovarov'
class shellsort(object):
    def issorted(self, a):
        for index in xrange(len(a)-1):
            if a[index] <= a[index+1]:
                continue
            else:
                raise AssertionError('array not sorted. %s' %str(a[index-5, index+5]))
    def sort(self):
        pass

