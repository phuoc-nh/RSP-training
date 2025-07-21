public class CPU {
    public void freeze() {
        System.out.println("Freezing CPU...");
    }
    public void jump(long position) {
        System.out.println("Jumping to position " + position);
    }
    public void execute() {
        System.out.println("Executing instructions...");
    }
}

public class Memory {
    public void load(long position, String data) {
        System.out.println("Loading data '" + data + "' at position " + position);
    }
}

public class HardDrive {
    public String read(long lba, int size) {
        return "Boot sector";
    }
}

public class ComputerFacade {
    private CPU cpu;
    private Memory memory;
    private HardDrive hardDrive;

    public ComputerFacade() {
        this.cpu = new CPU();
        this.memory = new Memory();
        this.hardDrive = new HardDrive();
    }

    public void startComputer() {
        cpu.freeze();
        String bootData = hardDrive.read(0, 1024);
        memory.load(0, bootData);
        cpu.jump(0);
        cpu.execute();
    }
}
