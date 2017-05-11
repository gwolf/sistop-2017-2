/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import org.hyperic.sigar.*;
import static java.lang.Thread.sleep;
import java.text.DecimalFormat;
/**
 *
 * @author Octavio
 */
public class Monitor implements Runnable{
    static int i=0;
    private static Sigar sigar = new Sigar(); // los metodos de sigar necesitan objetos para funcionar
    
    static    Mem mem = null;
    static    CpuPerc cpuperc = null;
    static    FileSystemUsage filesystemusage = null;


    private boolean usoMem = false; // flags para los semaforos
    private boolean usoCom = false;
    private boolean usoDisco = false;

    /**
     * @param args the command line arguments
     */
    public static void creaHilos() { // aqui creamos los hilos

        

        Monitor h1 = new Monitor();
        Thread thread = new Thread (h1, "Hilo 1");
        thread.start();

        Monitor h2 = new Monitor();
        Thread thread1 = new Thread (h2, "Hilo 2");
        thread1.start();

        Monitor h3 = new Monitor();
        Thread thread2 = new Thread (h3, "Hilo 3");
        thread2.start();
    
    }
    
    public void run(){ // aqui corremos
        
        ram();
        cpu();
        disco();
        
    }
    
    public synchronized int ram(){ // metodo para obtener uso de RAM
        i++;    
        while (usoMem) // solo uno a la vez
        {
            try
                {
                wait(); // bloqueamos acceso a otros threads
            }
            catch (Exception e) { }
        }
       
       try {
            mem = sigar.getMem();         
        } catch (SigarException se) {
            se.printStackTrace();
        }
        DecimalFormat df = new DecimalFormat("#.##");
         String por = df.format(mem.getUsedPercent());
       System.out.printf("\n %s Obtuvo el uso de memoria, es de: %s",Thread.currentThread().getName(),por );
       Aguanta(1,10);
        usoMem = true;
        usoCom=false; // bajamos el semaforo
        usoDisco=false;
        notifyAll(); // liberamos el candado
    return 1;
    } // end ram


public synchronized int cpu(){ // metodo para sacar el uso de CPU
    i++;
    while (usoCom) //solo un thread entra a la vez
    {
        try
        {
            wait(); // bloqueo acceso
        }
        catch (Exception e) { }
    }
    try {
            cpuperc = sigar.getCpuPerc();
         
        } 
    catch (SigarException se) {
            se.printStackTrace();
        }
    double porcentaje =(cpuperc.getCombined()*100);

   if(Double.isNaN(porcentaje)==false){ //valido que no entregue NaN como resultado valido.
        System.out.printf("\n %s Uso de cpu es: %.2f porciento",Thread.currentThread().getName(),porcentaje);
   }else{
        System.out.printf("\n %s No se pudo obtener el uso del cpu.",Thread.currentThread().getName());
   }
   Aguanta(1,10);
    usoMem = false;
    usoCom=true; // movemos las flags de nuestros semaforos
    usoDisco=false;
    notifyAll(); // liberamos el candado
return 1;
} // end cpu

  
      public synchronized int disco(){ //metodo para obtener uso de HDD
        i++;    
        while (usoDisco) //solo un thread entra a la vez
        {
            try
                {
                wait(); // bloqueamos acceso
            }
            catch (Exception e) { }
        }
       
       try {
            filesystemusage = sigar.getFileSystemUsage("C:");         
        } catch (SigarException se) {
            se.printStackTrace();
        }
       double disc= (filesystemusage.getUsePercent()*10);
       System.out.printf("\n %s Obtuvo el uso de disco, es de: %.2f",Thread.currentThread().getName(),disc );
       Aguanta(1,10);
       usoMem = false;
        usoCom=false;
        usoDisco=true;
        notifyAll();
    return 1; // ya pueden acceder otros threads
    } // end disco
      
    private void Aguanta(int min, int max) { // metodo que duerme los hilos cuando no les toca

        try {
            sleep(min + (int) (max * Math.random()));
        } catch (Exception e) {
        }
    } // este metodo deberia ser innecesario porque estoy usando wait();, pero no se por que si no lo agrego el programa falla a veces. Tal vez estan mal mis semaforos?
    
public static void main (String args[]){
        Monitor.i=0;
        Monitor.creaHilos();
    }
  
} 