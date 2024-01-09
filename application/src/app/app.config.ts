import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routing } from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [provideRouter(routing)]
};
