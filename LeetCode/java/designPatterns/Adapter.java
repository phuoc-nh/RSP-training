public interface UsbCable {
	void plug();
}

public class UsbPort {
    public void plug(UsbCable cable) {
        cable.plug();
    }
}

public class MicroUsbCable {
    private boolean isPlugged = false;

    public void plugMicroUsb() {
        isPlugged = true;
        System.out.println("Micro USB cable plugged in.");
    }
}

public class MicroUsbToUsbAdapter implements UsbCable {
    private MicroUsbCable microUsbCable;

    public MicroUsbToUsbAdapter(MicroUsbCable cable) {
        this.microUsbCable = cable;
    }

    @Override
    public void plug() {
        microUsbCable.plugMicroUsb(); // Adapt the incompatible method
    }
}

public class Main {
    public static void main(String[] args) {
        UsbPort usbPort = new UsbPort();

        // Use a regular USB cable
        UsbCable usbCable = () -> System.out.println("USB cable plugged in.");
        usbPort.plug(usbCable);

        // Use a Micro USB cable via adapter
        MicroUsbCable microUsbCable = new MicroUsbCable();
        UsbCable adapter = new MicroUsbToUsbAdapter(microUsbCable);
        usbPort.plug(adapter);
    }
}
