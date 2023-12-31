import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule, Routes } from '@angular/router'; 
import { AppComponent } from './app.component';
import { routing } from './app.routes'

const routes: Routes = [

]

@NgModule({
    declarations: [AppComponent],
    imports: [
      BrowserModule,
      HttpClientModule,
      RouterModule.forRoot(routing)
      //changed route to routing. did not change anything, but leaving for rn
    ],
    providers: [],
    bootstrap: [AppComponent]
  })
  export class AppModule { }