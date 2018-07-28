import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { GenerateSamplesComponent } from './generate/samples-and-semantics/generate.samples.component';
import { GenerateCommonComponent } from './generate/common-use-cases/generate.common.component';
import { GenerateInferenceComponent } from './generate/inference/generate.inference.component';
import { TutorialComponent } from './tutorial/tutorial.component';
import { ContactComponent } from './contact/contact.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'generate/samples', component: GenerateSamplesComponent },
  { path: 'generate/common', component: GenerateCommonComponent },
  { path: 'generate/inference', component: GenerateInferenceComponent },
  { path: 'tutorial', component: TutorialComponent },
  { path: 'contact', component: ContactComponent }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})

export class RoutingModule { }
