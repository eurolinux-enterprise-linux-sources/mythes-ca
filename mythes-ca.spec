Name: mythes-ca
Summary: Catalan thesaurus
Version: 1.5.0
Release: 8%{?dist}
Source: http://www.softcatala.org/diccionaris/actualitzacions/sinonims/thesaurus-ca.oxt
Group: Applications/Text
URL: http://www.softcatala.org/wiki/Projectes/Openthesaurus-ca
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPL+
BuildArch: noarch
Requires: mythes

%description
Catalan thesaurus.

%prep
%setup -q -c

%build
for i in release_note-ca.txt dictionaries/README_th_ca_ES_v3.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p dictionaries/th_ca_ES_v3.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_ca_ES_v2.dat
cp -p dictionaries/th_ca_ES_v3.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_ca_ES_v2.idx
pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
ca_ES_aliases="ca_AD ca_FR ca_IT"
for lang in $ca_ES_aliases; do
        ln -s th_ca_ES_v2.dat "th_"$lang"_v2.dat"
        ln -s th_ca_ES_v2.idx "th_"$lang"_v2.idx"
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc dictionaries/README_th_ca_ES_v3.txt LICENCES-fr.txt LICENSES-en.txt LICENCIAS-es.txt LLICENCIES-ca.txt release_note-ca.txt
%{_datadir}/mythes/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Apr 03 2010 Caolan McNamara <caolanm@redhat.com> - 1.5.0-4
- mythes now owns /usr/share/mythes

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolán McNamara <caolanm@redhat.com> - 1.5.0-2
- tidy spec

* Fri Mar 27 2009 Caolán McNamara <caolanm@redhat.com> - 1.5.0-1
- latest version

* Mon Mar 09 2009 Caolán McNamara <caolanm@redhat.com> - 1.0.0-1
- latest version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-0.2.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 06 2009 Caolán McNamara <caolanm@redhat.com> - 0.5.1-0.1.beta
- initial version
