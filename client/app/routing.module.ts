import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AboutComponent } from './about/about.component';
import { GenerateComponent } from './generate/generate.component';

const routes: Routes = [
  { path: '', component: AboutComponent },
  { path: 'generate', component: GenerateComponent }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})

export class RoutingModule {}
