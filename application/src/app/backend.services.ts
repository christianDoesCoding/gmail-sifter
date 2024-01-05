import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})

export class BackendService {

  constructor(private http: HttpClient) { }

  authenticate() {
    return this.http.get('http://localhost:5000/');
  }
}
// /login?