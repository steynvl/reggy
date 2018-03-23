import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AboutComponent } from './about/about.component';
import { GenerateSamplesComponent } from './generate/samples-and-semantics/generate.samples.component';

const routes: Routes = [
  { path: '', component: AboutComponent },
  { path: 'generate/samples', component: GenerateSamplesComponent }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})

export class RoutingModule {}
