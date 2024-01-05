import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { BackendService } from './backend.services'
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, HttpClientModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Gmail Sifter';

  constructor(private backendService: BackendService) {}

  gmailAuthenticate() {
    console.log('Button Clicked')
    this.backendService.authenticate().subscribe(
      (response: any) => { //need to edit response type
        console.log('authentication successful', response)
      },
      (error: any) => {
        console.log('authentication failed', error)
      }
    );
  }
}