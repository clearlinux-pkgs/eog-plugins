#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : eog-plugins
Version  : 3.26.3
Release  : 16
URL      : https://download.gnome.org/sources/eog-plugins/3.26/eog-plugins-3.26.3.tar.xz
Source0  : https://download.gnome.org/sources/eog-plugins/3.26/eog-plugins-3.26.3.tar.xz
Summary  : Plugins for Eye of Gnome
Group    : Development/Tools
License  : GPL-2.0
Requires: eog-plugins-data = %{version}-%{release}
Requires: eog-plugins-lib = %{version}-%{release}
Requires: eog-plugins-license = %{version}-%{release}
Requires: eog-plugins-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : gettext
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(eog)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gsettings-desktop-schemas)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libexif)
BuildRequires : pkgconfig(libgdata)
BuildRequires : pkgconfig(libpeas-1.0)

%description


%package data
Summary: data components for the eog-plugins package.
Group: Data

%description data
data components for the eog-plugins package.


%package lib
Summary: lib components for the eog-plugins package.
Group: Libraries
Requires: eog-plugins-data = %{version}-%{release}
Requires: eog-plugins-license = %{version}-%{release}

%description lib
lib components for the eog-plugins package.


%package license
Summary: license components for the eog-plugins package.
Group: Default

%description license
license components for the eog-plugins package.


%package locales
Summary: locales components for the eog-plugins package.
Group: Default

%description locales
locales components for the eog-plugins package.


%prep
%setup -q -n eog-plugins-3.26.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556996237
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1556996237
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/eog-plugins
cp COPYING %{buildroot}/usr/share/package-licenses/eog-plugins/COPYING
%make_install
%find_lang eog-plugins

%files
%defattr(-,root,root,-)
/usr/lib64/eog/plugins/exif-display.plugin
/usr/lib64/eog/plugins/export-to-folder.plugin
/usr/lib64/eog/plugins/export-to-folder.py
/usr/lib64/eog/plugins/fit-to-width.plugin
/usr/lib64/eog/plugins/fullscreenbg.plugin
/usr/lib64/eog/plugins/fullscreenbg.py
/usr/lib64/eog/plugins/hide-titlebar.plugin
/usr/lib64/eog/plugins/light-theme.plugin
/usr/lib64/eog/plugins/maximize-windows.plugin
/usr/lib64/eog/plugins/maximize-windows.py
/usr/lib64/eog/plugins/postasa.plugin
/usr/lib64/eog/plugins/pythonconsole.plugin
/usr/lib64/eog/plugins/pythonconsole/__init__.py
/usr/lib64/eog/plugins/pythonconsole/config.py
/usr/lib64/eog/plugins/pythonconsole/console.py
/usr/lib64/eog/plugins/send-by-mail.plugin
/usr/lib64/eog/plugins/slideshowshuffle.plugin
/usr/lib64/eog/plugins/slideshowshuffle.py

%files data
%defattr(-,root,root,-)
/usr/share/appdata/eog-exif-display.metainfo.xml
/usr/share/appdata/eog-export-to-folder.metainfo.xml
/usr/share/appdata/eog-fit-to-width.metainfo.xml
/usr/share/appdata/eog-fullscreenbg.metainfo.xml
/usr/share/appdata/eog-hide-titlebar.metainfo.xml
/usr/share/appdata/eog-light-theme.metainfo.xml
/usr/share/appdata/eog-maximize-windows.metainfo.xml
/usr/share/appdata/eog-postasa.metainfo.xml
/usr/share/appdata/eog-pythonconsole.metainfo.xml
/usr/share/appdata/eog-send-by-mail.metainfo.xml
/usr/share/appdata/eog-slideshowshuffle.metainfo.xml
/usr/share/eog/plugins/export-to-folder/preferences_dialog.ui
/usr/share/eog/plugins/fullscreenbg/preferences_dialog.ui
/usr/share/eog/plugins/pythonconsole/config.ui
/usr/share/glib-2.0/schemas/org.gnome.eog.plugins.exif-display.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.eog.plugins.export-to-folder.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.eog.plugins.fullscreenbg.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.eog.plugins.pythonconsole.gschema.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/eog/plugins/libexif-display.so
/usr/lib64/eog/plugins/libfit-to-width.so
/usr/lib64/eog/plugins/libhide-titlebar.so
/usr/lib64/eog/plugins/liblight-theme.so
/usr/lib64/eog/plugins/libpostasa.so
/usr/lib64/eog/plugins/libsend-by-mail.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/eog-plugins/COPYING

%files locales -f eog-plugins.lang
%defattr(-,root,root,-)

