package Enums;


public enum Places {
    Island("остров"),
    Corner("уголок"),
    Lawn("полянка"),
    Thicket("в чаще леса"),
    Forest("лес"),
    Home("домой"),
    Fence("ограда"),
    Paddock("загон");
    private final String place;
    Places(String place){
        this.place = place;
    }
    public String getPlace(){
        return place;
    }
}
