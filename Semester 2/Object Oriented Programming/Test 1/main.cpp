//
// Created by Cristi Ifrim on 4/6/2022.
//

#include "service.h"
#include "repository.h"
#include "ui.h"

int main() {

    Repository r;
    Service service{r};
    UI ui{service};

    ui.start();

}
