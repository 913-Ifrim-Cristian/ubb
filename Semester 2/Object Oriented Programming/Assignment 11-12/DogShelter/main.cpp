#include "gui.h"
#include <QtWidgets/QApplication>
#include "service.h"
#include "FileRepository.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    FileRepository repo{ "repo.txt" };

    AdminService admin{ repo };
    UserService user{ repo };

    GUI w{ admin, user };
    w.show();
    return a.exec();
}
