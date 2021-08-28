import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { ApiserviceService } from '../../servicios/apiservice.service';

//structure

@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
})
export class LoginPage {

  user = {
    usuario:'',
    password:''
  }

  constructor (){

  }
  /*resultado: any;
  
  constructor ( private servicio: ApiserviceService ){
    this.servicio.obtenerDatos(1).subscribe(
      (respuesta) => {
        this.resultado = JSON.stringify(respuesta);
      }
    )
  }*/
  
  login(user: string, pass:string ){
    if (user = this.user.usuario){
      return `routerLink="/inicio"`;
    }
  }

}
