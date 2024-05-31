#include <stdio.h>
#include <stdlib.h>
#include <sys/ioctl.h>
#include <fcntl.h>
#include <linux/cdrom.h>
#include <unistd.h>

int main() {
    int cdrom, status;
    while (1>0) {
      status=1;
      cdrom = open("/dev/sr0", O_RDONLY | O_NONBLOCK);
      if (ioctl(cdrom,CDROM_DRIVE_STATUS) == CDS_TRAY_OPEN) {
          status=0;
      }
      close(cdrom);
      if (status != 0) {
          system("eject -r 2> /dev/null");
      }
    }
}
