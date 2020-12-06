from pt import Pt
from st import St

class Pm:
    """ A physical memory that simulates physical memory.

    Attributes:
        _pm (:obj:`list` of int): List of integers, which represents physical memory.
        _st (:obj:`St`): Segment table object that helps mutate and access the segment table portion of _pm.
        _pt (:obj:'`Pt`): Page table object that helps mutate and access the page table portion of _pm.

    """

    def __init__(self):
        self._pm = [None]*524288
        temp = [None] * 512
        self._disk = [temp.copy() for i in range(1024)]
        self._availableFrames = [i for i in range(2,1024)]
        self._st = St(self._pm, self._disk, self._availableFrames)
        self._pt = Pt(self._pm, self._disk, self._availableFrames)

    def addSegments(self, s: str) -> None:
        """ Function that parses a string and add segment table entries accordingly.

        Args:
            s (string): String of multiple values in the order segment number, segment length, frame number.

        Returns:
            None

        """
        segList = s.split()
        for i in range(int(len(segList)/3)):
            self._st.addSeg(int(segList[i*3]), int(segList[i*3+1]), int(segList[i*3+2]))
        return None

    def addPages(self, s: str) -> None:
        """ Function that parses a string and adds page table entries accordingly.
        
        Args:
            s (string): String of multiple values in the order segment number, page number, frame number.

        Returns:
            None
        
        """

        pageList = s.split()
        for i in range(int(len(pageList)/3)):
            self._pt.addPag(int(pageList[i*3]), int(pageList[i*3+1]), int(pageList[i*3+2]))
        return None

    def lookup(self, s: int, p: int, w: int) -> int:
        """ Function that retrieves the physical address.

        Args:
            s (int): Segment number
            p (int): Page number
            w (int): Word offset

        Returns:
            int: Physical address of a given s,p,w

        Raises:
            ValueError if the segment does not have a page table or if a page does not have a frame

        """
        pt = self._st.frameNum(s)
        physicalA = self._pt.address(pt, p, w)
        return physicalA

