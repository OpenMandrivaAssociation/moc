%define _disable_ld_no_undefined 1

%define pre alfa4_svn2454

Summary:	Simple console audio player
Name:		moc
Version:	2.5.0
Release:	0.%{pre}.3
Epoch:		1
License:	GPLv2+
Group:		Sound
URL:		http://moc.daper.net/
Source0:	ftp://ftp.daper.net/pub/soft/moc/unstable/%{name}-%{version}_%{pre}.tar.gz
BuildRequires:	pkgconfig(ncurses++w)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(speex)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	libmpcdec-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	ffmpeg-devel >= 2.5.4
BuildRequires:	libfaac-devel
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(id3tag)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	db-devel
BuildRequires:	libtool-devel
BuildRequires:	autogen
BuildRequires:	pkgconfig(wavpack)
BuildRequires:	magic-devel
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	gettext-devel
BuildRequires:	libstdc++-devel

%description
MOC is a console audio player with ncurses interface
Features:
  * Supports aac ffmpeg flac modplug mp3 musepack sndfile speex vorbis wavpack
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
%setup -q -n trunk

%build
export CFLAGS="%{optflags} `pkg-config --cflags ncursesw`"
autoreconf -i

%configure2_5x 
%make

%install
%makeinstall_std
rm -rf %{buildroot}/usr/share/doc/
rm -rf %{buildroot}/%{_libdir}/*/*/*la

%files
%doc COPYING AUTHORS NEWS README TODO
%doc config.example keymap.example
%{_bindir}/mocp
%{_mandir}/*/*
%{_libdir}/%{name}
%{_datadir}/%{name}

