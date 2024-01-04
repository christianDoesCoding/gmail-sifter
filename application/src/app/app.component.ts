import { HttpClientModule } from '@angular/common/http';
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { BackendService } from '../../../../backend/backend.py'

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Gmail Sifter';

  constructor(private backendService: BackendService) {}

  gmailAuthenticate() {
    console.log('Button Clicked')
    this.backendService.authenticate().subscribe(
      (response: string) => { //may not be a string 
        console.log('authentication successful', response)
      },
      (error: any) => {
        console.log('authentication failed', error)
      }
    );
  }
}