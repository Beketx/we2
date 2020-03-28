import { Component } from '@angular/core';

import { products } from '../products';
import { Product } from '../products';
@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent {
  products = products;

  share(product: Product):void {
    window.open(`//api.whatsapp.com/send?phone=77478865590_NUMBER&text=${product.ref}`, "_blank");
  }
  onNotify(){
    window.alert('The product has been shared!');
  }
}


/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at http://angular.io/license
*/