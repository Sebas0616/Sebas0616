package Main;

import Logica.*;


public class Main {
    
    public static void tocar(IGuitarra[] a ){
            for(IGuitarra Gui : a){
                Gui.tocar();
            }
            System.out.println("\nTodas las guitarras estàn sonando\n");
    }
    
    public static void parar(IGuitarra[] a ){
            for(IGuitarra Gui : a){
                Gui.parar();
            }
            System.out.println("\nTodas las guitarras dejaron de sonar");
    }
    
    public static void main(String[] args) {
        
        IGuitarra[] gui = {
            new GuitarraA(),
            new GuitarraE()
        };
        
        tocar(gui);
        parar(gui);
    }
}
