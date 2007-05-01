%define version 2.4.1
%define rel 1

Summary: Simple console audio player
Name: moc
Version: %{version}
Release: %mkrel %{rel}
URL: http://moc.daper.net/
Source0: ftp://ftp.daper.net/pub/soft/%{name}/stable/%{name}-%{version}.tar.bz2
License: GPL
Group: Sound
BuildRequires: ncurses-devel mad-devel curl-devel
BuildRequires: speex-devel oggvorbis-devel libmpcdec-devel
BuildRequires: libalsa-devel 
# do not compile
#BuildRequires: libflac-devel 
BuildRequires: libid3tag-devel taglib-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
MOC is a console audio player with ncurses interface
Features:

        * Supports MP3, WAV, and OGG formats.
        * Play files from directory changing automatically to the next one
          without any playlist.
        * Supports id3tag, VBR and Xing header for MP3.
        * Simple mixer.
        * Fast switching to your music directory.
        * Playlists (without read/write to a file).
        * Shuffle and repeat.
        * Changing process priority to higher value.
        * Playing in separate thread.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

rm -rf $RPM_BUILD_ROOT/usr/share/doc/
rm -rf $RPM_BUILD_ROOT/%_libdir/*/*/*la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING AUTHORS NEWS README TODO
%doc config.example keymap.example 
%{_bindir}/mocp
%{_mandir}/*/*
%{_libdir}/%{name}/
%{_datadir}/%{name}/


