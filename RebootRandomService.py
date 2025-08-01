import os
import random
import win32event
import win32service
import win32serviceutil
import servicemanager

class RebootRandomService(win32serviceutil.ServiceFramework):
    _svc_name_        = "RebootRandomService"
    _svc_display_name_= "Random Interval Reboot Service"
    # make the service auto-start at boot
    _svc_start_type_  = win32service.SERVICE_AUTO_START

    def __init__(self, args):
        super().__init__(args)
        # event used to signal service stop
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        # report we're stopping and signal the loop to break
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)

    def SvcDoRun(self):
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, '')
        )
        self.main()

    def main(self):
        while True:
            # pick a random timeout between 10 and 60 minutes
            minutes = random.randint(10, 60)
            servicemanager.LogInfoMsg(
                f"{self._svc_name_}: next reboot in {minutes} minute(s)."
            )
            # wait that many minutes, or until stopped
            timeout_ms = minutes * 60 * 1000
            rc = win32event.WaitForSingleObject(self.stop_event, timeout_ms)
            if rc == win32event.WAIT_OBJECT_0:
                # stop requested
                servicemanager.LogInfoMsg(f"{self._svc_name_}: stop signal received.")
                break

            # time’s up → reboot
            servicemanager.LogInfoMsg(f"{self._svc_name_}: rebooting now.")
            # immediate reboot
            os.system("shutdown /r /t 0")
            # after shutdown command, Windows will reboot and restart this service

if __name__ == '__main__':
    # support: install, remove, start, stop, restart
    win32serviceutil.HandleCommandLine(RebootRandomService)
