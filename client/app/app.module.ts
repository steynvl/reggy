import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { JwtModule } from '@auth0/angular-jwt';

import { RoutingModule } from './routing.module';
import { SharedModule } from './shared/shared.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { TutorialComponent } from './tutorial/tutorial.component';
import { ContactComponent } from './contact/contact.component';

import { GenerateSamplesComponent } from './generate/samples-and-semantics/generate.samples.component';
import { GenerateCommonComponent } from './generate/common-use-cases/generate.common.component';
import { GenerateInferenceComponent } from './generate/inference/generate.inference.component';

import { GenerateService } from './services/generate.service';
import { VerificationService } from './services/verification.service';
import { ContactService } from './services/contact.service';
import { InferrerService } from './services/inferrer.service';

import { LiteralTextInfoComponent } from './samples-components/literal-text-info/literal-text-info.component';
import { BasicCharacterInfoComponent } from './samples-components/basic-characters-info/basic-characters-info.component';
import { DigitsInfoComponent } from './samples-components/digits-info/digits-info.component';
import { ControlCharactersInfoComponent } from './samples-components/control-characters-info/control-characters-info.component';
import { UnicodeCharactersInfoComponent } from './samples-components/unicode-characters-info/unicode-characters-info.component';
import { NumbersInfoComponent } from './samples-components/numbers-info/numbers-info.component';
import { MatchAnythingInfoComponent } from './samples-components/match-anything-info/match-anything-info.component';
import { ListOfLiteralTextInfoComponent } from './samples-components/list-of-literal-text-info/list-of-literal-text-info.component';

import { UsernameInfoComponent } from './common-use-case-components/username-info/username-info.component';
import { PasswordInfoComponent } from './common-use-case-components/password-info/password-info.component';
import { UrlInfoComponent } from './common-use-case-components/url-info/url-info.component';
import { EmailInfoComponent } from './common-use-case-components/email-info/email-info.component';
import { CreditCardInfoComponent } from './common-use-case-components/credit-card-info/credit-card-info.component';
import { VatNumberInfoComponent } from './common-use-case-components/vat-number-info/vat-number-info.component';
import { DateAndTimeInfoComponent } from './common-use-case-components/date-and-time-info/date-and-time-info.component';
import { GuidInfoComponent } from './common-use-case-components/guid-info/guid-info.component';
import { NationalIdInfoComponent } from './common-use-case-components/national-id-info/national-id-info.component';
import { Ipv4AddressInfoComponent } from './common-use-case-components/ipv4-address-info/ipv4-address-info.component';
import { CurrencyInfoComponent } from './common-use-case-components/currency-info/currency-info.component';

import { MarkedTextToView } from './pipes/marked-text-to-view';

import { ClipboardModule } from 'ngx-clipboard';
import { HighlightModule } from 'ngx-highlightjs';
import { DataTableModule } from 'angular5-data-table';

import { JavaComponent } from './language-examples/java/java.component';
import { PerlComponent } from './language-examples/perl/perl.component';

import { DndModule } from 'ng2-dnd';

export function tokenGetter() {
  return localStorage.getItem('token');
}

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    TutorialComponent,
    ContactComponent,
    GenerateSamplesComponent,
    GenerateCommonComponent,
    GenerateInferenceComponent,
    LiteralTextInfoComponent,
    BasicCharacterInfoComponent,
    DigitsInfoComponent,
    ControlCharactersInfoComponent,
    UnicodeCharactersInfoComponent,
    NumbersInfoComponent,
    MatchAnythingInfoComponent,
    ListOfLiteralTextInfoComponent,
    UsernameInfoComponent,
    PasswordInfoComponent,
    UrlInfoComponent,
    EmailInfoComponent,
    CreditCardInfoComponent,
    VatNumberInfoComponent,
    DateAndTimeInfoComponent,
    GuidInfoComponent,
    NationalIdInfoComponent,
    Ipv4AddressInfoComponent,
    CurrencyInfoComponent,
    MarkedTextToView,
    JavaComponent,
    PerlComponent
  ],
  imports: [
    RoutingModule,
    SharedModule,
    ClipboardModule,
    DataTableModule,
    HighlightModule.forRoot({
      path: 'assets/lib/highlight'
    }),
    JwtModule.forRoot({
      config: {
        tokenGetter: tokenGetter,
        // whitelistedDomains: ['localhost:3000', 'localhost:4200']
      }
    }),
    DndModule.forRoot()
  ],
  providers: [GenerateService,
              VerificationService,
              ContactService,
              InferrerService
  ],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  bootstrap: [AppComponent]
})

export class AppModule { }
