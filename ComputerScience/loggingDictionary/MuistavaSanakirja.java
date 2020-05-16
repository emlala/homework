/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sanakirja;

import java.io.File;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 *
 * @author Emmi
 */
public class MuistavaSanakirja {

    private Map<String, String> sanasto;
    private String tiedosto;

    public MuistavaSanakirja() {
        this.sanasto = new HashMap<>();
    }

    public MuistavaSanakirja(String tiedosto) {
        this.sanasto = new HashMap<>();
        this.tiedosto = tiedosto;
    }

    public void lisaa(String sana, String kaannos) {
        if (!this.sanasto.containsKey(sana)) {
            this.sanasto.put(sana, kaannos);
        }
    }

    public String kaanna(String sana) {
        if (this.sanasto.containsKey(sana)) {
            return this.sanasto.get(sana);
        } else if (this.sanasto.containsValue(sana)) {
            for (String s : this.sanasto.keySet()) {
                if (this.sanasto.get(s).equals(sana)) {
                    return s;
                }
            }
        }
        return null;
    }

    public void poista(String sana) {

        if (this.sanasto.containsKey(sana)) {
            this.sanasto.remove(sana);
        } else if (this.sanasto.containsValue(sana)) {
            sanasto.values().remove(sana);
        }
    }

    public boolean lataa() {
        try {
            Scanner tiedostonlukija = new Scanner(new File(this.tiedosto));
            while (tiedostonlukija.hasNextLine()) {
                String rivi = tiedostonlukija.nextLine();
                String[] osat = rivi.split(":");
                this.sanasto.put(osat[0], osat[1]);
            }
            tiedostonlukija.close();
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    public boolean tallenna() {
        try {
            PrintWriter tallentaja = new PrintWriter(new File(this.tiedosto));
            for (String k : this.sanasto.keySet()) {
                String v = this.sanasto.get(k);
                tallentaja.println(k + ":" + v);
            }
            tallentaja.close();
            return true;
        } catch (Exception e) {
            return false;
        }
    }
}
