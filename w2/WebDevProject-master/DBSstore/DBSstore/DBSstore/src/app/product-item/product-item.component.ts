import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { products } from '../products';
import {CartService} from '../cart.service';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent implements OnInit {
  product;


  addToCart(product) {
    this.cartService.addToCart(product);
    window.alert('Выбранный продукт добавлен в корзину!');
  }



  constructor(
    private route: ActivatedRoute,
    private cartService: CartService,
  ) { }

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      this.product = products[+params.get('productId') - 1];
    });
  }
}
