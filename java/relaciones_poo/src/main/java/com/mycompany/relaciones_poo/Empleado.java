/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.relaciones_poo;

/**
 *
 * @author Estudiante
 */
public class Empleado {
    
    public String nombre;
    public String cargo;
    
    public Empleado(String nombre,String cargo){
        this.nombre=nombre;
        this.cargo=cargo;
    }
    
    public String getNombre(){
        
        return nombre;
    }
    
    @Override
    public String toString(){
        return nombre;
    }
    
}
