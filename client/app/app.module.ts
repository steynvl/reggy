import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { JwtModule } from '@auth0/angular-jwt';

import { RoutingModule } from './routing.module';
import { SharedModule } from './shared/shared.module';
import { AppComponent } from './app.component';
import { AboutComponent } from './about/about.component';

import { GenerateSamplesComponent } from './generate/samples-and-semantics/generate.samples.component';
import { GenerateCommonComponent } from './generate/common-use-cases/generate.common.component';
import { GenerateInductionComponent } from './generate/induction/generate.induction.component';

import { GenerateSamplesService } from './services/generate.samples.service';
import { GenerateCommonService } from './services/generate.common.service';
import { GenerateInductionService } from './services/generate.induction.service';

import { MarkedTextInfoComponent } from './field-info/marked-text-info/marked-text-info.component';
import { BasicCharacterInfoComponent } from './field-info/basic-characters-info/basic-characters-info.component';
import { DigitsInfoComponent } from './field-info/digits-info/digits-info.component';
import { ControlCharactersInfoComponent } from './field-info/control-characters-info/control-characters-info.component';
import { UnicodeCharactersInfoComponent } from './field-info/unicode-characters-info/unicode-characters-info.component';

import { UsernameInfoComponent } from './common-use-case-components/username-info/username-info.component';
import { PasswordInfoComponent } from './common-use-case-components/password-info/password-info.component';
import { UrlInfoComponent } from './common-use-case-components/url-info/url-info.component';
import { EmailInfoComponent } from './common-use-case-components/email-info/email-info.component';
import { CreditCardInfoComponent } from './common-use-case-components/credit-card-info/credit-card-info.component';
import { VatNumberInfoComponent } from './common-use-case-components/vat-number-info/vat-number-info.component';

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
    GenerateCommonComponent,
    GenerateInductionComponent,
    MarkedTextInfoComponent,
    BasicCharacterInfoComponent,
    DigitsInfoComponent,
    ControlCharactersInfoComponent,
    UnicodeCharactersInfoComponent,
    UsernameInfoComponent,
    PasswordInfoComponent,
    UrlInfoComponent,
    EmailInfoComponent,
    CreditCardInfoComponent,
    VatNumberInfoComponent,
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
  providers: [GenerateSamplesService,
              GenerateCommonService,
              GenerateInductionService
  ],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  bootstrap: [AppComponent]
})

export class AppModule { }
