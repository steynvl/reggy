import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { JwtModule } from '@auth0/angular-jwt';

import { RoutingModule } from './routing.module';
import { SharedModule } from './shared/shared.module';
import { AppComponent } from './app.component';
import { AboutComponent } from './about/about.component';
import { GenerateSamplesComponent } from './generate/samples-and-semantics/generate.samples.component';
import { GenerateSamplesService } from './services/generate.samples.service';

import { MarkedTextInfoComponent } from './field-info/marked-text-info/marked-text-info.component';
import { BasicCharacterInfoComponent } from './field-info/basic-characters-info/basic-characters-info.component';
import { DigitsInfoComponent } from './field-info/digits-info/digits-info.component';
import { ControlCharactersInfoComponent } from './field-info/control-characters-info/control-characters-info.component';
import { UnicodeCharactersInfoComponent } from './field-info/unicode-characters-info/unicode-characters-info.component';

import { MarkedTextToView } from './pipes/marked-text-to-view';

import { ClipboardModule } from 'ngx-clipboard';
import { HighlightModule } from 'ngx-highlightjs';

import { JavaComponent } from './language-examples/java/java.component';
import { PerlComponent } from './language-examples/perl/perl.component';

export function tokenGetter() {
  return localStorage.getItem('token');
}

@NgModule({
  declarations: [
    AppComponent,
    AboutComponent,
    GenerateSamplesComponent,
    MarkedTextInfoComponent,
    BasicCharacterInfoComponent,
    DigitsInfoComponent,
    ControlCharactersInfoComponent,
    UnicodeCharactersInfoComponent,
    MarkedTextToView,
    JavaComponent,
    PerlComponent
  ],
  imports: [
    RoutingModule,
    SharedModule,
    ClipboardModule,
    HighlightModule.forRoot({
      path: 'assets/lib/highlight'
    }),
    JwtModule.forRoot({
      config: {
        tokenGetter: tokenGetter,
        // whitelistedDomains: ['localhost:3000', 'localhost:4200']
      }
    })
  ],
  providers: [GenerateSamplesService],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  bootstrap: [AppComponent]
})

export class AppModule { }
