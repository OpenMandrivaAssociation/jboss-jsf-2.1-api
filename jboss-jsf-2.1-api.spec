%{?_javapackages_macros:%_javapackages_macros}
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name: jboss-jsf-2.1-api
Version: 2.0.2
Release: 7.0%{?dist}
Summary: JavaServer Faces 2.1 API

License: CDDL or GPLv2 with exceptions
URL: http://www.jboss.org

# git clone git://github.com/jboss/jboss-jsf-api_spec.git jboss-jsf-2.1-api
# cd jboss-jsf-2.1-api/ && git archive --format=tar --prefix=jboss-jsf-2.1-api-2.0.2.Final/ jboss-jsf-api_2.1_spec-2.0.2.Final | xz > jboss-jsf-2.1-api-2.0.2.Final.tar.xz
Source0: %{name}-%{namedversion}.tar.xz

# Fix the FSF address in the license file:
Patch0: %{name}-fix-fsf-address.patch

BuildRequires: java-devel
BuildRequires: jboss-parent
BuildRequires: jpackage-utils
BuildRequires: geronimo-validation
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: objenesis
BuildRequires: jboss-el-2.2-api
BuildRequires: jboss-jsp-2.2-api
BuildRequires: jboss-jstl-1.2-api
%if 0%{?fedora}
%else
Buildequires:  bean-validation-api
%endif

Requires: jpackage-utils
Requires: jboss-jsp-2.2-api
Requires: jboss-jstl-1.2-api
Requires: jboss-el-2.2-api
Requires: geronimo-validation
Requires: java

BuildArch:noarch


%description
JavaServer(tm) Faces API classes based on Version 2.1 of Specification.


%package javadoc
Summary: Javadocs for %{name}

Requires: jpackage-utils


%description javadoc	
This package contains the API documentation for %{name}.


%prep

# Unpack the sources:
%setup -q -n %{name}-%{namedversion}


# Apply the patches:
%patch0 -p1


%build
mvn-rpmbuild install javadoc:aggregate


%install

# Jar files:
install -d -m 755 %{buildroot}%{_javadir}
install -pm 644 target/jboss-jsf-api_2.1_spec-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# Dependencies map:
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "javax.faces:jsf-api"

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}


%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc LICENSE
%doc README


%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE
%doc README


%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.0.2-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 28 2012 Juan Hernandez <juan.hernandez@redhat.com> 2.0.2-3
- Added geronimo-validation to the build requirements

* Fri Mar 23 2012 Juan Hernandez <juan.hernandez@redhat.com> 2.0.2-2
- Use global instead of define

* Thu Mar 22 2012 Juan Hernandez <juan.hernandez@redhat.com> 2.0.2-1
- Update to upstream version 2.0.0
- Cleanup of the spec file

* Fri Aug 12 2011 Marek Goldmann <mgoldman@redhat.com> 2.0.0-1
- Initial packaging

