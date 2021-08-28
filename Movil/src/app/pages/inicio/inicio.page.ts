import { Component, OnInit } from '@angular/core';
import { PopoverController } from '@ionic/angular';
import { PopinfoComponent } from '../../Componentes/popinfo/popinfo.component';

@Component({
  selector: 'app-inicio',
  templateUrl: './inicio.page.html',
  styleUrls: ['./inicio.page.scss'],
})
export class InicioPage implements OnInit {
  

  constructor( private popoverController: PopoverController) { }

  ngOnInit() {
  }

  async mostrarPop(){
    const popover = await this.popoverController.create({
      component:  PopinfoComponent
    });
    await popover.present();
  }
}
