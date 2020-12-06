class St:
    """ A segment table that simulates a segment table.

    Attributes:
        _pm (:obj:`list` of int): List of integers, which represents physical memory.
        _disk (:obj:`list` of :obj:`list` of int): List of list of integers, which represents disk blocks.
        _availableFrames (:obj:`list` of int): List of integers that represent available frames.

    """

    def __init__(self, pm: list, disk: list, af: list):
        self._pm = pm
        self._disk = disk
        self._availableFrames = af

    def addSeg(self, segN: int, segL: int, fraN: int):
        """ Function that adds a segment to physical memory.

        Args:
            segN (int): Segment number
            segL (int): Segment length
            fraN (int): Frame number

        Returns:
            None
        
        """
        self._pm[2*segN] = segL
        self._pm[(2*segN)+1] = fraN
        if (fraN > 0):
            self._availableFrames.pop(self._availableFrames.index(fraN))
        return None

    def frameNum(self, s: int) -> int:
        """ Function that returns the frame number of a given segment's page table.

        Args:
            s (int): Segment number

        Returns:
            int: Frame number of segment s's page table

        Raises:
            ValueError in the event that a segment does not have a page table.

        """
        fn = self._pm[(2*s)+1]
        if (fn == None):
            raise ValueError
        elif (fn < 0):
            next = self._availableFrames.pop(0)
            self._pm[(2*s)+1] = next
            for i in range(512):
                self._pm[(next*512)+i] = self._disk[-1*fn][i]
            fn = next
        return fn
