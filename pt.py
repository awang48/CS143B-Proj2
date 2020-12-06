class Pt:
    """ A page table that simulates a page table.

    Attributes:
        _pm (:obj:`list` of int): List of integers, which represents physical memory.
        _disk (:obj:`list` of :obj:`list` of int): List of list of integers, which represents disk blocks.
        _availableFrames (:obj:`list` of int): List of integers that represent available frames.

    """

    def __init__(self, pm: list, disk: list, af: list):
        self._pm = pm
        self._disk = disk
        self._availableFrames = af

    def addPag(self, segN: int, pagN: int, fraN: int) -> None:
        """ Function that adds a page to physical memory.

        Args:
            segN (int): Segment number
            pagN (int): Page number
            fraN (int): Frame number

        Returns:
            None

        """

        fn = self._pm[(2*segN)+1]
        if (fn < 0):
            self._disk[-1*fn][pagN] = fraN
            if (fraN > 0):
                self._availableFrames.pop(self._availableFrames.index(fraN))
        else:
            self._pm[(fn*512)+pagN] = fraN
            if (fraN > 0):
                self._availableFrames.pop(self._availableFrames.index(fraN))
        return None

    def address(self, pt: int, p: int, w: int) -> int:
        """ Function that returns the address of a given word.

        Args:
            pt (int): Frame number of page table
            p (int): Page number
            w (int): Word number

        Returns:
            int: Address of a the desired word

        Raises:
            ValueError in the event that a frame is not allocated to a page.

        """
        fn = self._pm[(pt*512)+p]
        if (fn == None):
            raise ValueError
        elif (fn < 0):
            next = self._availableFrames.pop(0)
            self._pm[(pt*512)+p] = next
            fn = next
        return (fn*512)+w