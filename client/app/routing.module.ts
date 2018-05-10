import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AboutComponent } from './home/home.component';
import { GenerateSamplesComponent } from './generate/samples-and-semantics/generate.samples.component';
import { GenerateCommonComponent } from './generate/common-use-cases/generate.common.component';
import { GenerateInductionComponent } from './generate/induction/generate.induction.component';
import { TutorialComponent } from './tutorial/tutorial.component';
import { ContactComponent } from './contact/contact.component';

const routes: Routes = [
  { path: '', component: AboutComponent },
  { path: 'generate/samples', component: GenerateSamplesComponent },
  { path: 'generate/common', component: GenerateCommonComponent },
  { path: 'generate/induction', component: GenerateInductionComponent },
  { path: 'tutorial', component: TutorialComponent },
  { path: 'contact', component: ContactComponent }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})

export class RoutingModule {}
