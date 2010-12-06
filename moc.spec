%define _disable_ld_no_undefined 1

Summary:	Simple console audio player
Name:		moc
Version:	2.4.4
Release:	%mkrel 7
License:	GPLv2+
Group:		Sound
URL:		http://moc.daper.net/
Source0:	ftp://ftp.daper.net/pub/soft/%{name}/stable/%{name}-%{version}.tar.bz2
Patch1:		moc-2.4.3-fix-str-fmt.patch
BuildRequires:	ncursesw-devel
BuildRequires:	mad-devel
BuildRequires:	curl-devel
BuildRequires:	speex-devel
BuildRequires:	oggvorbis-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	libalsa-devel
BuildRequires:	libflac-devel
BuildRequires:	sndfile-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	id3tag-devel
BuildRequires:	taglib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
MOC is a console audio player with ncurses interface
Features:

        * Supports MP3, WAV, FLAC, and OGG formats.
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
%patch1 -p0

%build
export CFLAGS="%{optflags} `pkg-config --cflags ncursesw`"
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -rf %{buildroot}/usr/share/doc/
rm -rf %{buildroot}/%{_libdir}/*/*/*la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING AUTHORS NEWS README TODO
%doc config.example keymap.example
%{_bindir}/mocp
%{_mandir}/*/*
%{_libdir}/%{name}
%{_datadir}/%{name}
