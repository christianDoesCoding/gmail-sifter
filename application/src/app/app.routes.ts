/*import all components for app here*/
import { Routes } from '@angular/router';
import { AppComponent } from './app.component'

/*
where the different routes of the application will go
{ path: '/routeName', component: componentName }
*/
export const routes: Routes = [
    { path:'', component: AppComponent}, //remove '' path
];
