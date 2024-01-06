import { Component } from '@angular/core';
import { BackendService } from './backend.services'

@Component({
  selector: 'app-root',
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